# visualyzer_types/set_module.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Set:
    def __init__(self, shapes, top_width=5, bottom_width=7, height=4):
        self.shapes = shapes
        self.top_width = top_width
        self.bottom_width = bottom_width
        self.height = height
        self.facecolor = 'None'

        max_shapes = max(len(shapes),8)
        
#         fig_width = len(shapes) * (bottom_width + 1)
#         fig_height = 2 * height
        fig_width = max_shapes * (bottom_width + 1)
        fig_height = 2 * height

        self.fig, self.ax = plt.subplots(figsize=(fig_width, fig_height))
        self.ax.axis([0, fig_width, -height, height])
       # plt.axis("scaled")
        plt.axis("off")

        self.create_background()
        self.create()

    def triangle_list(self, center_x, center_y, shape, top_label, bottom_label):
        # Calculate the coordinates of the three corners of the triangle
        x1 = center_x
        y1 = center_y + self.height / 2
        x2 = center_x - self.bottom_width / 2
        y2 = center_y - self.height / 2
        x3 = center_x + self.bottom_width / 2
        y3 = center_y - self.height / 2

        triangle = patches.Polygon(
            [(x1, y1), (x2, y2), (x3, y3)],
            closed=True,
            facecolor=self.facecolor,
            edgecolor='black',
            linewidth=8
        )
        self.ax.add_patch(triangle)

        # Adjust the shape size and position to fit within the triangle
        shape_size = 0.5 * min(self.top_width, self.height)  # Adjust shape size

        if isinstance(shape, str) and len(shape) == 1:
            circle = patches.Circle((center_x, center_y), radius=shape_size/4, facecolor='black', edgecolor='black', linewidth=8)
            self.ax.add_patch(circle)
            
        elif type(shape) == str:
    # Adjust the circle radius and position
            circle_radius = shape_size / 4
            circle_offset = shape_size / 3  # Adjust this value as needed to fit within the triangle

            circle1 = patches.Circle((center_x - circle_offset, center_y), radius=circle_radius, facecolor='black', edgecolor='black', linewidth=8)
            circle2 = patches.Circle((center_x + circle_offset, center_y), radius=circle_radius, facecolor='black', edgecolor='black', linewidth=8)
            self.ax.add_patch(circle1)
            self.ax.add_patch(circle2)

    # Draw a line connecting the circles
            self.ax.plot([center_x - circle_offset, center_x + circle_offset], [center_y, center_y], color='black', linewidth=8)


        elif type(shape) in [int, float, complex]:
            rhombus = patches.Polygon(
                [(center_x, center_y + shape_size/3),
                 (center_x - shape_size/3, center_y),
                 (center_x, center_y - shape_size/3),
                 (center_x + shape_size/3, center_y)],
                facecolor='black',
                edgecolor='black',
                linewidth=8)
            self.ax.add_patch(rhombus)

        # ... continue with adjustments for other types (set, True, False, None, list)
                    # ... continue with adjustments for other types (set, True, False, None, list)
        elif type(shape) == set:
                small_triangle_size = shape_size / 2
                small_triangle = patches.Polygon(
                    [(center_x, center_y + small_triangle_size), 
                     (center_x - small_triangle_size, center_y - small_triangle_size), 
                     (center_x + small_triangle_size, center_y - small_triangle_size)],
                    facecolor='None', edgecolor='black', linewidth=8)
                self.ax.add_patch(small_triangle)
            
        elif shape == True:
                arrow_up = patches.FancyArrow(center_x, center_y - shape_size / 2, 0, shape_size, head_width=shape_size / 3, head_length=shape_size / 3, fc='black', ec='black', linewidth=8)
                self.ax.add_patch(arrow_up)
        elif shape == False:
                arrow_down = patches.FancyArrow(center_x, center_y + shape_size / 2, 0, -shape_size, head_width=shape_size / 3, head_length=shape_size / 3, fc='black', ec='black', linewidth=8)
                self.ax.add_patch(arrow_down)

        elif shape is None:
                circle_None = patches.Circle((center_x, center_y), radius=shape_size / 2, facecolor='None', edgecolor='black', linewidth=8)
                self.ax.add_patch(circle_None)
                line_start_x = center_x - shape_size / 2
                line_start_y = center_y - shape_size / 2
                line_end_x = center_x + shape_size / 2
                line_end_y = center_y + shape_size / 2
                self.ax.plot([line_start_x, line_end_x], [line_start_y, line_end_y], color='black', linewidth=8)
        
        elif type(shape) == list:
            rect_width = shape_size * 0.4  # Adjust the width of the rectangle
            rect_height = shape_size * 0.6  # Adjust the height of the rectangle
            rect_offset = shape_size / 3  # Adjust this value as needed to fit within the triangle

    # Calculate positions for the rectangles
            rect1_x = center_x - rect_offset - rect_width / 2
            rect1_y = center_y - rect_height / 2
            rect2_x = center_x + rect_offset - rect_width / 2
            rect2_y = center_y - rect_height / 2

    # Create rectangles
            rect1 = patches.Rectangle((rect1_x, rect1_y), width=rect_width, height=rect_height, facecolor='None', edgecolor='black', linewidth=8)
            rect2 = patches.Rectangle((rect2_x, rect2_y), width=rect_width, height=rect_height, facecolor='None', edgecolor='black', linewidth=8)
            self.ax.add_patch(rect1)
            self.ax.add_patch(rect2)

    # Draw a line connecting the rectangles
            self.ax.plot([center_x - rect_offset+0.4, center_x + rect_offset-0.4], [center_y, center_y], color='black', linewidth=8)
    
    
        elif type(shape) == tuple:
            para_width = shape_size * 0.3  # Adjust the width of the parallelogram
            para_height = shape_size * 0.5  # Adjust the height of the parallelogram
            para_offset = shape_size / 3  # Adjust this value as needed
            skew_factor = para_width * 0.7  # Adjust to skew the parallelogram

            para1_points = [
               (center_x - para_offset - skew_factor, center_y - para_height / 2),  # Bottom left
               (center_x - para_offset + para_width - skew_factor, center_y - para_height / 2),  # Bottom right
               (center_x - para_offset + para_width, center_y + para_height / 2),  # Top right
               (center_x - para_offset, center_y + para_height / 2)  # Top left
                   ]
        
            para2_points = [
               (center_x + para_offset - skew_factor, center_y - para_height / 2),  # Bottom left
               (center_x + para_offset + para_width - skew_factor, center_y - para_height / 2),  # Bottom right
               (center_x + para_offset + para_width, center_y + para_height / 2),  # Top right
               (center_x + para_offset, center_y + para_height / 2)  # Top left
                   ]
            para1 = patches.Polygon(para1_points, closed=True, facecolor='None', edgecolor='black', linewidth=8)
            para2 = patches.Polygon(para2_points, closed=True, facecolor='None', edgecolor='black', linewidth=8)
            self.ax.add_patch(para1)
            self.ax.add_patch(para2)

    # Draw a line connecting the parallelograms
            self.ax.plot([center_x - para_offset + para_width - skew_factor+0.25, center_x + para_offset - skew_factor+0.15], [center_y, center_y], color='black', linewidth=8)
    
    
    def create_background(self):
        background_width = len(self.shapes) * (self.bottom_width + 0.1)
        background_height = 2 * self.height
        rectangle = patches.Rectangle(
            (0, -self.height),
            width=background_width,
            height=background_height,
            facecolor="None",
            edgecolor='None',
            linewidth=2
        )
        self.ax.add_patch(rectangle)
    def create(self):
        positions = [i * (self.bottom_width + 1) for i in range(len(self.shapes))]
        centers = []
        
        for i, shape in enumerate(self.shapes):
            center_x = positions[i] + self.bottom_width / 2
            center_y = 0
            top_label = i
            bottom_label = i - len(self.shapes)
            self.triangle_list(center_x, center_y, shape, top_label, bottom_label)
            centers.append((center_x, center_y))

    # Add connection lines between the edges of triangles
        for i in range(len(centers) - 1):
            x1, y1 = centers[i][0] + self.bottom_width / 2, centers[i][1] - self.height / 2  # Right edge of the left triangle
            x2, y2 = centers[i + 1][0] - self.bottom_width / 2, centers[i + 1][1] - self.height / 2  # Left edge of the right triangle
            self.ax.plot([x1, x2], [y1, y2], color='black', linewidth=8)

    plt.show()


