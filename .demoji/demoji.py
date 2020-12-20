from PIL import Image
import sys

img = Image.open(f"{sys.argv[1]}.png")
w,h = img.size

if(w/h >= 1):
    rszd_img = img.resize((int(48*w/h),48))
else:
    rszd_img = img.resize((48,int(48*h/h)))
    
rszd_img.save(f"/home/zilch/.emojis/{sys.argv[1]}.png")
