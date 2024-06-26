SELECT distinct
vrs.Name0 [Computer Name], vgos.Caption0 [OS],vrs.User_Name0 [User Name],
IIf([EnforcementState]=1001,'Installation Success',
IIf([EnforcementState]>=1000 And [EnforcementState]<2000 And [EnforcementState]<>1001,'Installation Success',
IIf([EnforcementState]>=2000 And [EnforcementState]<3000,'In Progress', IIf([EnforcementState]>=3000 And [EnforcementState]<4000,'Requirements Not Met ', IIf([EnforcementState]>=4000 And [EnforcementState]<5000,'Unknown', IIf([EnforcementState]>=5000 And [EnforcementState]<6000,'Error','Unknown')))))) AS Status
FROM dbo.v_R_System AS vrs
INNER JOIN (dbo.vAppDeploymentResultsPerClient
INNER JOIN v_CIAssignment
ON dbo.vAppDeploymentResultsPerClient.AssignmentID = v_CIAssignment.AssignmentID)
ON vrs.ResourceID = dbo.vAppDeploymentResultsPerClient.ResourceID
INNER JOIN dbo.fn_ListApplicationCIs(1033) lac
ON lac.ci_id=dbo.vAppDeploymentResultsPerClient.CI_ID
INNER JOIN dbo.v_GS_WORKSTATION_STATUS AS vgws
ON vgws.ResourceID=vrs.resourceid
INNER JOIN v_FullCollectionMembership coll
ON coll.ResourceID = vrs.ResourceID
INNER JOIN dbo.v_GS_OPERATING_SYSTEM AS vgos
ON vgos.ResourceID = vrs.ResourceID
WHERE lac.DisplayName= 'XXXXXXXXXX'
and CollectionName = 'XXXXXXXXXX'