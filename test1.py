paths = glob.glob("./DICOM/0009455/*.dcm")

dwi_files = []
for path in paths:
    if re.search("DWI",path):
        dwi_files.append(path)



for dwi_file in dwi_files:

    dwi = pydicom.read_file(dwi_file)

    image = dwi.pixel_array