import nibabel as nib
import matplotlib.pyplot as plt
import streamlit as st
class Image3D:
    def __init__(self,path):
        self.path = path
        self.img = nib.load(self.path)
        self.current_silce = 0
        self.nii_data = self.img.get_fdata()
        self.current_fig = None

    def update_path(self,path):
        self.path = path
        self.img = nib.load(self.path)
        self.current_silce = 0
        self.nii_data = self.img.get_fdata()
        self.current_fig = None

    def increment_slice_number(self):
        self.current_silce +=1

    def get_next_slice(self):
        return self.nii_data[:,:,self.current_silce]
    
    def get_given_slice(self,slice_nr):
        return self.nii_data[:,:,slice_nr]

    def plot_from_given_slice(self,sl):
        fig, ax = plt.subplots()
        im = ax.imshow(self.get_given_slice(sl))
        return fig
    def plot_from_current_slice(self):
        fig, ax = plt.subplots()
        im = ax.imshow(self.get_given_slice(self.current_silce))
        return fig
    def get_both_slices(self,x,y):
        return self.nii_data[:,:,y],self.nii_data[:,x,:]

    def plot_both_slices(self,x,y):
        y_array, x_array = self.get_both_slices(x,y)
        fig, ax = plt.subplots(2)
        im = ax[0].imshow(x_array)
        im = ax[1].imshow(y_array)
        return fig


