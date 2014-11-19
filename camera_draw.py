from SimpleCV import Camera, Display
from SimpleCV import Color, Image, DrawingLayer

disp = Display((1440, 900))
#disp = Display((640, 480))

# Initialize the camera
cam = Camera(0, {"width":1280, "height":780})

displaytype = 0


# Loop to continuously get images
while(disp.isNotDone()):
    # Get Image from camera
	img = cam.getImage().flipHorizontal()

	color_blue = Color()
	color_blue = (13, 106, 251)

	blue = img.colorDistance(Color.HOTPINK).invert()
	blue_bin = blue.binarize((140,140,140)).invert()
	blue_bin = blue_bin.erode(3)
	blue_bin = blue_bin.dilate(3)

	blobs = blue_bin.findBlobs()
	
	if blobs:
		circles = blobs.filter([b.isCircle(0.5) for b in blobs])
		if circles and circles[-1].radius() > 3:
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(), Color.RED, 2)
			blue_bin.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(), Color.RED, 2)
			print "circle found at " + str(circles[-1].x) + " " + str(circles[-1].y) + " " +  str(circles[-1].radius())
	
	if disp.mouseRight:
		displaytype = displaytype ^ 1
		
	if displaytype:
		blue_bin.save(disp)
	else:
		img.save(disp)
	
			
	#blue_bin.save(disp)
	#img.addDrawingLayer(blue_bin)
	
	#b = blue_bin.findBlobs()
	#if b is not None:
	#	if b[0].area() > 10:
	#		xy = b[0].centroid()
	#		img2[xy[0],xy[1]] = (255, 255, 255)
			

	
	
	
	#img.addDrawingLayer(layer)
	#img.show()
	#img2.show()
	#blobs = blue_bin.findBlobs()
	#if blobs is not None:
	#	for b in blobs:
	#		if b.isCircle:
	#			#b.draw()
	#			img.save(disp)
	#			b.show()
	
	#b.save(disp)
	
    
	

    
    