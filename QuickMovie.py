import imdb
import wx
from wx import xrc

class MyApp(wx.App):

    def OnInit(self):
        self.res = xrc.XmlResource('QuickMovie.xrc')
        self.init_frame()
        return(True)

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'frameMain')
        
        self.favicon = wx.Icon('film.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        self.frame.SetIcon(self.favicon)    

        # Bind Controls
        self.txtTitle = xrc.XRCCTRL(self.frame, 'txtTitle')
        self.listCast = xrc.XRCCTRL(self.frame, 'listCast')
        self.txtYear = xrc.XRCCTRL(self.frame, 'txtYear')
        self.txtDirector = xrc.XRCCTRL(self.frame, 'txtDirector')
        self.txtRunTime = xrc.XRCCTRL(self.frame, 'txtRunTime')
        self.txtPlot = xrc.XRCCTRL(self.frame, 'txtPlot')
        self.btnSearch = xrc.XRCCTRL(self.frame, 'btnAnother')
        self.btnExit = xrc.XRCCTRL(self.frame, 'wxID_EXIT')
        self.statusBar = xrc.XRCCTRL(self.frame, 'statusBar')

        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_EXIT'))
        self.frame.Bind(wx.EVT_CLOSE, self.OnExitApp)
        self.Bind(wx.EVT_BUTTON, self.OnSearchClick, self.btnSearch)
        self.txtTitle.Bind(wx.EVT_KEY_DOWN, self.OnTitleChange)        
        
        self.frame.Show()

    def get_movie (self, title):
        myCursor= wx.StockCursor(wx.CURSOR_WAIT)
        self.frame.SetCursor(myCursor)
        self.statusBar.SetStatusText('Searching ...')
        
        # Create the object that will be used to access the IMDb's database.
        # By default access the web.
        ia = imdb.IMDb()
        
        # Search for a movie (get a list of Movie objects).
        s_result = ia.search_movie(title)
        
        # Only interested in the first result
        movie = s_result[0]
        ia.update(movie)
        
        self.txtTitle.SetValue('%s' % movie['title'])
        self.txtYear.SetValue('%s' % movie['year'])
        self.txtDirector.SetValue('%s' % movie['director'][0])
        self.txtRunTime.SetValue('%s min' % movie['runtime'][0])
        self.txtPlot.SetValue('%s' % movie['plot outline'])
        
        for item in movie['cast']:
            self.listCast.Append('%s' % item['name'])
            
        # self.listCast.SetSelection(0)
            
        # Set mousepointer to normal
        myCursor= wx.StockCursor(wx.CURSOR_ARROW)
        self.frame.SetCursor(myCursor)            
        self.statusBar.SetStatusText('Ready')    
        
    def clear_fields(self):
        self.txtDirector.SetValue('')
        self.txtRunTime.SetValue('')
        self.txtPlot.SetValue('')
        self.txtYear.SetValue('')
        self.listCast.Clear()
         
    def OnSearchClick(self, event): 
        self.title = self.txtTitle.GetValue()
        if self.title == '':
            self.statusBar.SetStatusText("Title is required")
            self.txtTitle.SetFocus()       
        else:
            self.get_movie(self.title)
     
    def OnTitleChange(self, event): 
        # Clear all other fields if title is changed and director is not already empty
        if self.txtDirector <> '':
            self.clear_fields()
        event.Skip()    
                 
    def OnClose(self, evt):
        self.Exit()
        
    def OnExitApp(self, event):
        self.Exit()
        
if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
