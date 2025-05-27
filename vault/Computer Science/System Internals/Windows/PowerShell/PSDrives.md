# PowerShell Drives (PSDrives)

**PowerShell Drives (PSDrives)** are abstractions of file systems which allow one to access and treat various data stores as if they were file systems.

[[PowerShell]] provides a few PSDrives by default. 

|PSDrive|Meaning|
|:--:|:--:|
|File System Drives (`C`, `D`, etc.)|These are direct mappings to the file system drives.|
|Registry Drives (`HKCU`, `HKLM`)|These correspond to the keys in the Windows registry.|
|`Cert`|Stores all installed certificates.|
|`Env`|Contains all environment variables.|
|`Variables`|Stores all defined variables.|
|`Functions`|Contains all defined functions.|

To navigate to a path within a PowerShell drive, you need to add a colon (`:`) to its name - for example `C:\`, `Env:\`, etc.

## Managing PSDrives

>[!TIP]- How-To: View PSDrives
>
>To view all available PowerShell drives:
>
>```powershell
>Get-PSDrive
>```
>
>![[res/View PSDrives.png]]
>

>[!TIP]- How-To: Create PSDrives
>
>To create a PSDrive you need to specify a name, a provider (`FileSystem` for a drive stored on the file system and `Registry` for a drive stored in the Windows Registry) and a root location for the drive.
>
>```powershell
>New-PSDrive -Name <Name> -PSProvider <Provider> -Root <Path>
>```
>
>![[res/Create PS Drive.png]]
>

>[!TIP]- How-To: Delete PSDrive
>
>You will first need to change to a different drive than the one you want to delete. Then just run:
>
>```powershell
>Remove-PSDrive -Name <Name>
>```
>
>![[res/Remove PSDrive.png]]
>