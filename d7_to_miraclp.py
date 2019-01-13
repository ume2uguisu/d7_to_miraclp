import tempfile
import zipfile
import os
import sys
import shutil
import xml.etree.ElementTree as ET

target_name = os.path.basename(sys.argv[1]).replace('.cws', '')

with tempfile.TemporaryDirectory() as temp_dir:
  with zipfile.ZipFile(sys.argv[1]) as existing_zip:
    existing_zip.extractall(temp_dir)
    files = os.listdir(temp_dir)

    for file in files:
      new_file_name = file.replace('mango3d', target_name)
      os.rename(os.path.join(temp_dir,file), os.path.join(temp_dir, new_file_name))

    with open(os.path.join(temp_dir, 'default.slicing'), mode='w') as f:
      f.write('')
    with open(os.path.join(temp_dir, 'hoge.stl'), mode='w') as f:
      f.write('')

    tree = ET.parse(os.path.join(temp_dir, 'manifest.xml'))
    root = tree.getroot()

    mname = ET.Element('name')
    mname.text = 'hoge'
    tag = ET.Element('tag')
    tag.text = '0'
    model = ET.Element('model')
    model.append(mname)
    model.append(tag)
    models = ET.Element('Models')
    models.append(model)

    root.append(models)

    sname = ET.Element('name')
    sname.text = 'default.slicing'
    sliceprofile = ET.Element('SliceProfile')
    sliceprofile.append(sname)
    root.append(sliceprofile)

    slice_names = root.findall('Slices/Slice/name')
    for slice_name in slice_names:
      slice_name.text = slice_name.text.replace('mango3d', target_name)

    gcode_name = root.find('GCode/name')
    gcode_name.text = gcode_name.text.replace('mango3d', target_name) 

    tree.write(os.path.join(temp_dir, 'manifest.xml'))

    shutil.copy2(sys.argv[1], sys.argv[1] + '.backup')

    with zipfile.ZipFile(sys.argv[1], 'w', compression = zipfile.ZIP_DEFLATED) as new_cws:
      for target_file in os.listdir(temp_dir):
        new_cws.write(os.path.join(temp_dir, target_file), arcname = target_file)
