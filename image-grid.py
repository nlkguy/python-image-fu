from PIL import Image
import os , glob



# get images path func
image_paths = [] # globa

def getImagePaths():
    folder_path = "/home/nlk/ProjectsX/testHostelsScrap/" 
    img_list = []
    if os.path.exists(folder_path):
        png_files = glob.glob(os.path.join(folder_path, '*.png'))

        for png_file in png_files:
            
            count+=1
            print(count)            
            image_paths.append(png_file)

        print(count)
        print(len(image_paths))
        
    else:
        print(f"no such folda!!: {folder_path}")


#-----------------------------------

getImagePaths()

tile_size = (18, 15)  # size of each img tile , in px

# for blank canvas , width, height in px
collage_width = 3210
collage_height = 3852 
# asper my calculation , for 45848 images , this tile size and canvas size is ideal , might change diffrent sizes in future
collage = Image.new('RGB', (collage_width, collage_height))


x, y = 0, 0 # position of tile
count = 0
for image_path in image_paths:
    image = Image.open(image_path)
    image = image.resize(tile_size, Image.ANTIALIAS)#resize img
    count+=1
    print(count)
    collage.paste(image, (x, y)) #paste tile/img to pos
    x += tile_size[0]
    if x + tile_size[0] > collage_width: # move down at rightt edge
        x = 0
        y += tile_size[1]

    if count%10000==0:
        collage.save(f"{count}_collage.jpg") # save img at intervals

collage.save("my_collage.jpg")
collage.show()














# old code , diffrent approach , didnt work properly
"""
image_size = (3852,3210)
rows = 21
columns =21
print("rows and colums defined")

collage_width = columns * image_size[0]
collage_height = rows * image_size[1]
collage = Image.new('RGB', (collage_width, collage_height))

print("before image loop")

for i, image_path in enumerate(image_paths):
    img = Image.open(image_path)
    img = img.resize(image_size, Image.ANTIALIAS) # problem is here ig
    print(i)
    row = i // columns
    col = i % columns
    
    x = col * image_size[0]
    y = row * image_size[1]
    
    collage.paste(img, (x, y))
    if i%4500==0:
        collage.show()
        collage.save('c1.jpg')

"""