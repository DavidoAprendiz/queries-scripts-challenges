$appxs = @( 
	"Microsoft.SkypeApp"
)

$appxprovisionedpackage = Get-AppxProvisionedPackage -Online
foreach ($app in $apps) {
    Get-AppxPackage -Name $app -AllUsers | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue

    ($appxprovisionedpackage).Where( {$_.DisplayName -EQ $app}) |
        Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue
}