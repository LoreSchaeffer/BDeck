const {app, BrowserWindow} = require('electron')
const path = require('path')

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 1000,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        },
        icon: path.join(__dirname, '/contents/images/icons/icon.ico'),
        minWidth: 1000,
        minHeight: 659,
        maxWidth: 1000,
        maxHeight: 659,
        maximizable: false
        //frame: false
    })

    mainWindow.loadFile(path.join(__dirname, '/contents/index.html'))
    mainWindow.removeMenu()

    // Open the DevTools.
    mainWindow.webContents.openDevTools()
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', function () {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit()
})