# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['TickerCode.py'],
             pathex=['/Users/brandonsoukup/Desktop/BTCTicker copy 2/venv/include'],
             binaries=[],
             datas=[],
             hiddenimports=['tkinter'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='TickerCode',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='btclogo.icns')
app = BUNDLE(exe,
             name='TickerCode.app',
             icon='btclogo.icns',
             bundle_identifier=None,
		info_plist={'NSHighResolutionCapable': 'True'})
