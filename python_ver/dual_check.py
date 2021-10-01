# pip install wxPython
import wx
 
app = wx.App()
 
#To get the count of displays
num_displays = wx.Display.GetCount()
 
print(num_displays)
# #Open a frame on each display
# for display_num in range(num_displays):
#     #Get a display object
#     display = wx.Display(display_num)
 
#     #To get a wx.Rect that gives the geometry of a display
#     geometry = display.GetxGeometry()
 
#     #Create a frame on the display
#     frame = wx.Frame(None,-1,"Display %d"%display_num,
#     geometry.GetTopLeft(),geometry.GetSize())
 
#     #Make the frame visible
#     frame.Show()
 
# app.MainLoop()