# -*- mode: python -*-

block_cipher = None


a = Analysis(['noconsole', 'converter.py'],
             pathex=['F:\\06_Python\\Workspace\\TAP4python\\TestCode'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='noconsole',
          debug=False,
          strip=False,
          upx=True,
          console=True )
