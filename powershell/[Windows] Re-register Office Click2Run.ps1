Set-ItemProperty -Path “HKLM:\SOFTWARE\Policies\Microsoft\office\16.0\common\officeupdate” -Name GPOOfficeMgmtCOM -Value 0 -Type DWord
Set-ItemProperty -Path “HKLM:\SOFTWARE\Policies\Microsoft\office\16.0\common\officeupdate” -Name OfficeMgmtCOM -Value 0 -Type DWord

Get-Service | where {$_.Name -like "*ClickToRunSvc*"} | Restart-Service

Set-ItemProperty -Path “HKLM:\SOFTWARE\Policies\Microsoft\office\16.0\common\officeupdate” -Name GPOOfficeMgmtCOM -Value 1 -Type DWord
Set-ItemProperty -Path “HKLM:\SOFTWARE\Policies\Microsoft\office\16.0\common\officeupdate” -Name OfficeMgmtCOM -Value 1 -Type DWord

Get-Service | where {$_.Name -like "*ClickToRunSvc*"} | Restart-Service
