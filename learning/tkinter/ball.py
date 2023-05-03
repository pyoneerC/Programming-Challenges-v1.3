class Ball:

    # ball characteristics
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    # move characteristics
    def move(self):
        coordinates = self.canvas.coords(self.image)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity # bounce (invert y if touching border)
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity #bounce (invert y if touching border)

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)