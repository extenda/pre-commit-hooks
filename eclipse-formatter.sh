#!/usr/bin/env bash

files=""
source="1.8"
target="1.8"

for i in "$@"; do
  case $i in
    --source=*)
      source="${i#*=}"
      shift
      ;;
    --target=*)
      target="${i#*=}"
      shift
      ;;
    *)
      files="$files,$i"
      shift
      ;;
  esac
done

if [ -z "$files" ]; then
  exit 0
fi

pom_dir="target/.eclipse-formatter"
pom_file="$pom_dir/.eclipse-formatter-pom.xml"

mkdir -s "$pom_dir" >/dev/null 2>&1

cat << EOF >> "$pom_file"
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>se.extenda.maven</groupId>
  <artifactId>eclipse-formatter</artifactId>
  <version>0</version>
  <build>
    <plugins>
      <plugin>
        <groupId>net.revelc.code.formatter</groupId>
        <artifactId>formatter-maven-plugin</artifactId>
        <version>2.7.1</version>
        <configuration>
          <directories>
            <directory>../</directory>
          </directories>
          <compilerCompliance>${source}</compilerCompliance>
          <compilerSource>${source}</compilerSource>
          <compilerTargetPlatform>${target}</compilerTargetPlatform>
          <lineEnding>LF</lineEnding>
          <encoding>UTF-8</encoding>
          <useEclipseDefaults>true</useEclipseDefaults>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
EOF

mvn -B -f "$pom_file" formatter:format -Dformatter.includes="${files:1}"
rm -f "$pom_file" || exit 0
