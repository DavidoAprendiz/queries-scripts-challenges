lazy val sonatypePublic = "Sonatype Public" at "https://oss.sonatype.org/content/groups/public/"
lazy val sonatypeReleases = "Sonatype Releases" at "https://oss.sonatype.org/content/repositories/releases/"
lazy val sonatypeSnapshots = "Sonatype Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots/"

addCompilerPlugin("org.typelevel" %% "kind-projector" % "0.10.3" cross CrossVersion.binary)
		
lazy val myResolvers = Seq(
	Resolver.mavenLocal,
	sonatypeReleases,
	sonatypeSnapshots,
	Resolver.mavenCentral
)

lazy val commonSettings = Seq(
	name := "pin_lock",
	organization := "portugal.ergo",
	version := "0.1.0",
	scalaVersion := "2.12.10",
)

lazy val myLibraries = Seq(
	"org.ergoplatform" %% "ergo-playground-env" % "0.0.0-65-c91117ae-SNAPSHOT"
)

lazy val myOptions = Seq(
	"-language:higherKinds",
	"-deprecation",
	"-encoding", "UTF-8",
  "-feature",
  "-unchecked"
)

lazy val root = (project in file("."))
	.settings(
		commonSettings,
		libraryDependencies ++= myLibraries,
		scalacOptions ++= myOptions,
		resolvers ++= myResolvers
)
