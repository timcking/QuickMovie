import wx
from wx import xrc
from wx.lib.dialogs import ScrolledMessageDialog 

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
        except Exception, e:
            print "headshot not found"        
        try:           
            for item in s_result['trivia']:
                self.listTrivia.Append('%s' % item)
        except Exception, e:
            print "trivia not found"             
            
        self.frame.Show()        
    
    def OnListTriviaClick(self, evt):
        # Note, using self.frame for ScrolledMessageDialog
        # TODO: Need to use a dict for trivia
        dialog = ScrolledMessageDialog (self.frame, 'Trivia Goes Here', 'Trivia', pos=wx.DefaultPosition, size=(450, 250))
        result = dialog.ShowModal()         
        
    def OnClose(self, evt):
        self.frame.Destroy()    