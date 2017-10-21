# Image processing #1
def main():
	# import the necessary packages
	import cv2
	 
	# load the image and show it
	image = cv2.imread("jurassic-park-tour-jeep.jpg")
	cv2.imshow("original", image)
	cv2.waitKey(0)

if __name__ == "__main__":
    main()