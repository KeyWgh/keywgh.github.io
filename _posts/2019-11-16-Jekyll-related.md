---
layout: post
title:  "Jekyll related topics"
date:   2019-11-16 16:17:55 -0500
categories: tools


---

Some problems I met when constructing website, along with my solutions.

## Images

### Rotation caused by EXIF info contained in metadata. 
 To fix it we can use python: 

```python
from PIL import Image
image_file = ""
im = Image.open(image_file)
im.transpose(Image.ROTATE_270).save(image_file)  # Change 270 to any degree you want
```

To see the details of EXIF:

```python
from PIL.ExifTags import TAGS
for tag, value in im._getexif().items():
		print(f"{:20s} {value})")
```

### Alignment

For multiple figures, the best way is to create a customized div by html. Control figure size by img tag.

```html
<div id="row">
<div class="column">
<figure >
<img  src=""  width="200px">
<figcaption style="text-align: left;" > Left </figcaption></figure></div>
<div class="column" >
<figure >
<img  src=""  width="200px" >
<figcaption style="text-align: left"> Right </figcaption></figure></div>
</div>
```

For parallel figure and text, using kramdown syntax is enough:

```markdown
![](..){:  width="300px" style="float: left; margin-right:5%"} 

Some text float to the right.
```

