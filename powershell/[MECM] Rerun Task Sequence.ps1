$TSID = "XXXXXXXX"
Get-WmiObject -Namespace "root\ccm\scheduler" -Class ccm_scheduler_history | where {$_.ScheduleID -like "*$TSID*"} | ft ScheduleID # Outputs the Schedule ID
Get-WmiObject -Namespace "root\ccm\scheduler" -Class ccm_scheduler_history | where {$_.ScheduleID -like "*$TSID*"} | Remove-WmiObject # Deletes the Schedule
Get-WmiObject -Namespace "root\ccm\scheduler" -Class ccm_scheduler_history | where {$_.ScheduleID -like "*$TSID*"} | ft ScheduleID # No output confirms the deletion
Get-Service | where {$_.Name -eq "CCMExec"} | Restart-Service # Restart the SMS Agent Host service