SELECT R.ResourceID, R.ResourceType, R.Name, R.SMSUniqueIdentifier, R.ResourceDomainORWorkgroup, R.Client
FROM SMS_R_System AS r full JOIN SMS_R_System AS s1 ON s1.ResourceId = r.ResourceId full JOIN SMS_R_System AS s2 ON s2.Name = s1.Name
WHERE s1.Name = s2.Name AND s1.ResourceId != s2.ResourceId
ORDER BY r.MACAddresses