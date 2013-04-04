import wx
from wx import xrc
from wx.lib.dialogs import ScrolledMessageDialog 
import urllib
from cStringIO import StringIO

class Person(wx.Frame):
    dictTrivia = {}
    
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
        self.listTrivia = xrc.XRCCTRL(self.frame, 'listTrivia')
        self.lblName.SetLabel("%s" % s_result['name'])
        
        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_CLOSE'))
        self.frame.Bind(wx.EVT_LISTBOX, self.OnListTriviaClick, id=xrc.XRCID('listTrivia'))
        
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
            fp = urllib.urlopen(s_result['headshot'])
            data = fp.read()
            fp.close()
            img = wx.ImageFromStream(StringIO(data))            
            bmp = wx.BitmapFromImage(img)
            self.bmpPic.SetBitmap(bmp)            
        except Exception, e:
            print "headshot not found"        
        try:           
            index_count = 0
            for item in s_result['trivia']:
                self.listTrivia.Append('%s' % item)
                # Save for when trivia is clicked
                self.dictTrivia[index_count] = item
                index_count += 1                    
        except Exception, e:
            print "trivia not found"             
            
        self.frame.Show()        
    
    def OnListTriviaClick(self, evt):
        selected = self.listTrivia.GetSelection()
        trivia = self.dictTrivia[selected]
        
        dialog = ScrolledMessageDialog (self.frame, trivia, 'Trivia', pos=wx.DefaultPosition, size=(450, 250))
        
        # Change the font from 8 (default) to 10
        children = dialog.GetChildren() 
        textCtrl = children[0] 
        textCtrl.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)) 
        
        result = dialog.ShowModal()         
        
    def OnClose(self, evt):
        self.frame.Destroy()    