GET-SERVICE -NAME WUAUSERV | STOP-SERVICE

Remove-Item -path "C:\Windows\System32\GroupPolicy\Machine\Registry.pol" -Force -ErrorAction SilentlyContinue
Remove-Item -path "C:\Windows\SOFTWAREDISTRIBUTION" -Force -Recurse -ErrorAction SilentlyContinue

GET-SERVICE -NAME WUAUSERV | START-SERVICE

Invoke-WMIMethod -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000021}" #Request Machine Assignments 
Invoke-WMIMethod -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000022}" #Evaluate Machine Policies 
Invoke-WMIMethod -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000113}" #Scan by Update Source
Invoke-WMIMethod -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000108}" #Software Updates Assignments Evaluation Cycle  
