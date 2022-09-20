#finding the centre of mass between point masses in three dimensional space
"""mass located at x,y,z"""
class MASS_XYZ:
    def __init__(this,my_mass, my_x, my_y, my_z):
        this.mass = my_mass
        this.x    = my_x
        this.y    = my_y
        this.z    = my_z

"""two point masses link"""
class MASS_LINK:
    def __init__(this,m1xyz,m2xyz):
        this.m1 = m1xyz.mass
        this.x1 = m1xyz.x
        this.y1 = m1xyz.y
        this.z1 = m1xyz.z
        this.m2 = m2xyz.mass
        this.x2 = m2xyz.x
        this.y2 = m2xyz.y
        this.z2 = m2xyz.z
        this.mass = this.m1 + this.m2
        this.comx = (this.x1) + ((this.x2)-(this.x1))*((this.m2)/((this.m1)+(this.m2)))
        this.comy = (this.y1) + ((this.y2)-(this.y1))*((this.m2)/((this.m1)+(this.m2)))
        this.comz = (this.z1) + ((this.z2)-(this.z1))*((this.m2)/((this.m1)+(this.m2)))


    
