import wx
import wx.adv

class SystemTrayIcon(wx.adv.TaskBarIcon):

    def __init__(self, iconPath, tooltip, openGui, menuItems):
        super(SystemTrayIcon, self).__init__()
        self.openGui = openGui

        self.setIcon(iconPath, tooltip)
        self.menu = self.createPopupMenu(menuItems)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.onLeftClick)
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.onRightClick)

    def setIcon(self, iconPath, tooltip):
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(iconPath, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon, tooltip)

    def createMenuItem(self, menu, label, func):
        item = wx.MenuItem(menu, wx.ID_ANY, label)
        menu.Bind(wx.EVT_MENU, lambda event: self.runFunc(event, func), id=item.GetId())
        menu.Append(item)
        return item

    def createPopupMenu(self, menuItems):
        menu = wx.Menu()
        for item in menuItems:
            if item == "separator":
                menu.AppendSeparator()
            else:
                self.createMenuItem(menu, item[0], item[1])
        return menu

    def runFunc(self, e, func):
        func()

    def onLeftClick(self, e):
        self.openGui()

    def onRightClick(self, e):
        self.PopupMenu(self.menu)