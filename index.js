const { app, BrowserWindow } = require('electron')
const { ElectronBlocker, fullLists, Request } = require('@cliqz/adblocker-electron')
const { readFileSync, writeFileSync } = require('fs')
const { fetch } = require('cross-fetch');

async function createWindow () {
  const win = new BrowserWindow({
    width: 1800,
    height: 1000,
    webPreferences: {
      webviewTag: true
    }
  })
  const blocker = await ElectronBlocker.fromLists(
    fetch,
    fullLists,
    {
      enableCompression: true,
    },
    {
      path: 'engine.bin',
      read: async (...args) => readFileSync(...args),
      write: async (...args) => writeFileSync(...args),
    },
  );
  blocker.enableBlockingInSession(win.webContents.session);
  win.loadFile('index.html')
}
// app.allowRendererProcessPeuse = false;

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})