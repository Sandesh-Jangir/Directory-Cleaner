import os

def createIfNotExists(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

files = os.listdir()
files.remove("Main.py")
createIfNotExists('Images')
createIfNotExists('Docs')
createIfNotExists('Others')

imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
docExts = [".txt", ".docx", ".pptx", ".xlsx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

other = []
for file in files:
  ext = os.path.splitext(file)[1].lower()
  if (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
    other.append(file)

for image in images:
  os.replace(image, f"Images/{image}")

for doc in docs:
  os.replace(doc, f"Docs/{doc}")

for otherf in other:
  os.replace(otherf, f"Others/{otherf}")