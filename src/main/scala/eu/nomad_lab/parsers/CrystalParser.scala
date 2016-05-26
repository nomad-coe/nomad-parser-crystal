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
  cmd = Seq(DefaultPythonInterpreter.python2Exe(), "${envDir}/parsers/crystal/parser/parser-crystal/crystalparser/scalainterface.py",
    "${mainFilePath}"),
  cmdCwd = "${mainFilePath}/..",
  resList = Seq(
    "parser-crystal/crystalparser/versions/crystal14/__init__.py",
    "parser-crystal/crystalparser/versions/crystal14/mainparser.py",
    "parser-crystal/crystalparser/versions/__init__.py",
    "parser-crystal/crystalparser/versions/versionsetup.py",
    "parser-crystal/crystalparser/__init__.py",
    "parser-crystal/crystalparser/parser_crystal.py",
    "parser-crystal/crystalparser/setup_paths.py",
    "parser-crystal/crystalparser/scalainterface.py",
    "nomad_meta_info/public.nomadmetainfo.json",
    "nomad_meta_info/common.nomadmetainfo.json",
    "nomad_meta_info/meta_types.nomadmetainfo.json",
    "nomad_meta_info/crystal.nomadmetainfo.json"
  ) ++ DefaultPythonInterpreter.commonFiles(),
  dirMap = Map(
    "parser-crystal" -> "parsers/crystal/parser/parser-crystal",
    "nomad_meta_info" -> "nomad-meta-info/meta_info/nomad_meta_info"
  ) ++ DefaultPythonInterpreter.commonDirMapping()
)
