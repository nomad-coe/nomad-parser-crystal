/*
 * Copyright 2016-2018 Sami Kivistö, Lauri Himanen, Fawzi Mohamed, Ankit Kariryaa
 * 
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 * 
 *     http://www.apache.org/licenses/LICENSE-2.0
 * 
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

package eu.nomad_lab.parsers

import eu.{ nomad_lab => lab }
import eu.nomad_lab.DefaultPythonInterpreter
import org.{ json4s => jn }
import scala.collection.breakOut

object CrystalParser extends SimpleExternalParserGenerator(
  name = "CrystalParser",
  parserInfo = jn.JObject(
    ("name" -> jn.JString("CrystalParser")) ::
      ("parserId" -> jn.JString("CrystalParser" + lab.CrystalVersionInfo.version)) ::
      ("versionInfo" -> jn.JObject(
        ("nomadCoreVersion" -> jn.JObject(lab.NomadCoreVersionInfo.toMap.map {
          case (k, v) => k -> jn.JString(v.toString)
        }(breakOut): List[(String, jn.JString)])) ::
          (lab.CrystalVersionInfo.toMap.map {
            case (key, value) =>
              (key -> jn.JString(value.toString))
          }(breakOut): List[(String, jn.JString)])
      )) :: Nil
  ),
  mainFileTypes = Seq("text/.*"),
  mainFileRe = """\s*[\*]{22,}
\s*\*\s{20,}\*
\s*\*\s{10,}CRYSTAL(?<majorVersion>[\d]+)\s{10,}\*
\s*\*\s{10,}public \: (?<minorVersion>[\d\.]+) \- .*\*
""".r, // [A-Z]{1}[a-z]{2} [\d]+[a-z]{2}, [\d]{4}[ ]{10,}\*
  cmd = Seq(DefaultPythonInterpreter.pythonExe(), "${envDir}/parsers/crystal/parser/parser-crystal/crystalparser/scalainterface.py",
    "${mainFilePath}"),
  cmdCwd = "${mainFilePath}/..",
  resList = Seq(
    "parser-crystal/crystalparser/versions/crystal14/__init__.py",
    "parser-crystal/crystalparser/versions/crystal14/mainparser.py",
    "parser-crystal/crystalparser/versions/crystal14/inputparser.py",
    "parser-crystal/crystalparser/versions/__init__.py",
    "parser-crystal/crystalparser/__init__.py",
    "parser-crystal/crystalparser/parser.py",
    "parser-crystal/crystalparser/setup_paths.py",
    "parser-crystal/crystalparser/scalainterface.py",
    "nomad_meta_info/public.nomadmetainfo.json",
    "nomad_meta_info/common.nomadmetainfo.json",
    "nomad_meta_info/meta.nomadmetainfo.json",
    "nomad_meta_info/crystal.nomadmetainfo.json"
  ) ++ DefaultPythonInterpreter.commonFiles(),
  dirMap = Map(
    "parser-crystal" -> "parsers/crystal/parser/parser-crystal",
    "nomad_meta_info" -> "nomad-meta-info/meta_info/nomad_meta_info"
  ) ++ DefaultPythonInterpreter.commonDirMapping()
)
