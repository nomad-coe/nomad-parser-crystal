package eu.nomad_lab.parsers

import org.specs2.mutable.Specification

object CrystalParserSpec extends Specification {
  "Cp2kParserTest" >> {
    "test with json-events" >> {
      ParserRun.parse(Cp2kParser, "parsers/crystal/test/examples/...", "json-events") must_== ParseResult.ParseSuccess
    }
  }

  "test with json" >> {
    ParserRun.parse(Cp2kParser, "parsers/crystal/test/examples/...", "json") must_== ParseResult.ParseSuccess
  }
}
