import wx
import wx.adv

class PopMenu(wx.Menu):
  
    def __init__(self, parent):
        super(PopMenu, self).__init__()
  
        self.parent = parent
  
        # menu item 1
        popmenu = wx.MenuItem(self, wx.NewId(), 'one ')
        self.Append(popmenu)
        # menu item 2
        popmenu2 = wx.MenuItem(self, wx.NewId(), 'two')
        self.Append(popmenu2)
 
class CustomTaskBarIcon(wx.adv.TaskBarIcon):
    """"""
 
    def __init__(self, frame):
        """Constructor"""
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
 
        icon = wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon, "Restore")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick) 
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.OnTaskBarRightClick)
    
    def InitUI(self):
  
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
  
        self.SetSize((600, 400))
        self.SetTitle('Popup Menu')
        self.Centre()

    def OnTaskBarActivate(self, evt):
        """"""
        pass
 
    def OnTaskBarClose(self, evt):
        """
        Уничтожает иконку панели задач и рамку в самой иконке панели задач
        """
        self.frame.Close()
 
    def OnTaskBarLeftClick(self, evt):
        self.frame.Show()
        self.frame.Restore()

    def OnTaskBarRightClick(self, evt):
        self.PopupMenu(PopMenu(self), evt.GetPosition())


class MainFrame(wx.Frame):
    """"""
 
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Minimize to Tray")
        panel = wx.Panel(self)
        self.tbIcon = CustomTaskBarIcon(self)
 
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)
 
        self.Show()
 
    def onClose(self, evt):
        """
        Уничтожает иконку панели задач и рамку
        """
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()
 
    def onMinimize(self, event):
        """
        Во время сворачивания, делаем так, чтобы приложение оставило иконку в трее
        """
        if self.IsIconized():
            self.Hide()
 
 
def main():
    """"""
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
 
if __name__ == "__main__":
    main()