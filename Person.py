import wx
from wx import xrc

class Person(wx.Frame):

    def __init__(self, s_result):
        self.res = xrc.XmlResource('Person.xrc')
        self.init_frame(s_result)
        
    def init_frame(self, s_result):
        self.frame = self.res.LoadFrame(None, 'framePerson')
        
        # Bind Controls
        self.lblName = xrc.XRCCTRL(self.frame, 'lblName')
        self.bmpPic = xrc.XRCCTRL(self.frame, 'bmpPic') 
        self.txtBirthName = xrc.XRCCTRL(self.frame, 'txtBirthName')
        self.txtBirthDate = xrc.XRCCTRL(self.frame, 'txtBirthDate')
        self.txtBirthPlace = xrc.XRCCTRL(self.frame, 'txtBirthPlace')
        self.txtBio = xrc.XRCCTRL(self.frame, 'txtBio')
        
        self.lblName.SetLabel("%s" % s_result['name'])
        
        # TODO, display headshot, see wxPython book
        # self.bmpPic.SetBitmap(wx.Bitmap('Veronica.jpg'))
        # Below does not work
        # self.bmpPic.SetBitmap(wx.Bitmap(s_result['headshot']))
        
        try:
            self.txtBirthName.SetValue('%s' % s_result['birth name'])
        except Exception, e:
            print "birth name not found"
        try:
            self.txtBirthDate.SetValue('%s' % s_result['birth date'])
        except Exception, e:
            print "birth date not found"
        try:
            self.txtBirthPlace.SetValue('%s' % s_result['birth notes'])
        except Exception, e:
            print "birth notes not found"
        try:
            self.txtBio.SetValue('%s' % s_result['mini biography'][0])
        except Exception, e:
            print "mini biography not found"
        try:
            print s_result['headshot']
        except Exception, e:
            print "headshot not found"        
            
        self.frame.Show()        
        
    def OnClose(self, evt):
        self.Close()    