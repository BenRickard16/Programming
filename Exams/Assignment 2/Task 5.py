from matplotlib import pyplot as plt

def lines_intersect(line1, line2):
    a = line1[0]
    b = line1[1]
    c = line1[2]
    d = line2[0]
    e = line2[1]
    f = line2[2]
    if b*d != a*e:
        x = (c*e - b*f) / (b*d - a*e)
        y = (a*f - c*d) / (b*d - a*e)
        return [x,y]
    
def point_on_segment(point, seg):
    seg1 = seg[0]
    seg2 = seg[1]
    v1 = [seg1[0] - point[0], seg1[1] - point[1]]
    v2 = [seg2[0] - point[0], seg2[1] - point[1]]
    dotpdct = v1[0]*v2[0] + v1[1]*v2[1]
    return dotpdct < 0


def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg[1]
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color = col)


def draw_line_in_window(line, window, col):
    windowx = window[0]
    windowy = window[1]
    x1 = windowx[0]
    x2 = windowx[1]
    y1 = windowy[0]
    y2 = windowy[1]
    wln1 = [1, 0, -1*x1]
    wln2 = [0, 1, -1*y2]
    wln3 = [1, 0, -1*x2]
    wln4 = [0, 1, -1*y1]
    
    p1 = lines_intersect(line, wln1)
    p2 = lines_intersect(line, wln2)
    p3 = lines_intersect(line, wln3)
    p4 = lines_intersect(line, wln4)
    
    seg1 = []
    if p1 != None:
        if point_on_segment(p1, [[x1, y1], [x1, y2]]):
            seg1.append(p1)
    if p2 != None:
        if point_on_segment(p2, [[x1, y2], [x2, y2]]):
            seg1.append(p2)
    if p3 != None:
        if point_on_segment(p3, [[x2, y1], [x2, y2]]):
            seg1.append(p3)
    if p4 != None:
        if point_on_segment(p4, [[x1, y1], [x2, y1]]):
            seg1.append(p4)
    if len(seg1) == 2:
        draw_segment(seg1, col)
        

    
    
        
    
        
    
    
    
        
    