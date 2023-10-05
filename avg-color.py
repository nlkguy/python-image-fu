import cv2 , os , glob, numpy



def calc_avg_clr(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    average_color = numpy.mean(image_rgb, axis=(0, 1))
    print(average_color)
    return average_color.astype(int)




folder_path = "/home/nlk/ProjectsX/testHostelsScrap/" 
count = 0
img_list = []
avg_color_list = []
if os.path.exists(folder_path):
    # use glob to get png files list
    png_files = glob.glob(os.path.join(folder_path, '*.png'))

    for png_file in png_files:
        count+=1
        img_list.append(png_file)
        clr = calc_avg_clr(png_file)
        print(clr)
        avg_color_list.append(clr)

    print(count)
    print(len(avg_color_list))
    
else:
    print(f"no folda!!: {folder_path}")


width, height = 1920,1080 # can change accorginf to # try current/50 and remove x50 repeatation below
image = numpy.zeros((height, width, 3), dtype=numpy.uint8)

ccc = 0
for y in range(height):
    step = 0
    for x in range(width):
        # repeat same color for 50 times in a line
        if step<50:
            image[y, x] = avg_color_list[ccc]
            step+=1
        else:
            ccc +=1
            step=0
        

cv2.imshow('avg color img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('colored_image.png', image)
