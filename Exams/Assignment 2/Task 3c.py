def line_from_segment(seg):
    p1 = seg[0]
    p2 = seg[1]
    a = p1[0]
    b = p1[1]
    c = p2[0]
    d = p2[1]
    return [d-b, a-c, b*c-a*d]

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

def segments_intersect(seg1, seg2):
    line1 = line_from_segment(seg1)
    line2 = line_from_segment(seg2)
    point = lines_intersect(line1, line2)
    if point_on_segment(point, seg1) and point_on_segment(point, seg2):
        return point
    

                               