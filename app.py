
import streamlit as st
import matplotlib.pyplot as plt
from nii import Image3D
import time
tick = time.time()
image = Image3D("avg152T1_LR_nifti.nii.gz")
print("Time taken: {}".format(time.time()-tick))
option_ph = st.empty()
filename_ph = st.empty()
slider_ph1 = st.empty()
slider_ph2 = st.empty()
image_ph = st.empty()
def main():
    global image
    path = filename_ph.text_input("File name",'avg152T1_LR_nifti.nii.gz')
    option = option_ph.selectbox(
                                    'Select view mode',
                                    ('Manual', 'Automatic')
                                )
    if image.path != path:
        image.update_path(path)
    if(len(image.nii_data.shape)==3):
        if option == 'Manual':
            print(image.nii_data.shape[2],image.nii_data.shape[1])
            sl1 = slider_ph1.slider('Select y_dim', 0, image.nii_data.shape[2],0,1)
            sl2 = slider_ph2.slider('Select x_dim', 0, image.nii_data.shape[1],0,1)
            fig = image.plot_both_slices(sl2,sl1)
            image_ph.pyplot(fig)
        else:
            for i in range(0,image.nii_data.shape[2]): 
                fig = image.plot_from_current_slice()
                sl1 = slider_ph1.slider('Select slide', 0, image.nii_data.shape[2],image.current_silce,1)
                image_ph.pyplot(fig)
                image.increment_slice_number()

if __name__ == "__main__":
    main()