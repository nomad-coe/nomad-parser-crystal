package eu.nomad_lab.parsers

import org.specs2.mutable.Specification

object CrystalParserSpec extends Specification {
  "CrystalParserTest" >> {
    "test with json-events" >> {
      ParserRun.parse(CrystalParser, "parsers/crystal/test/examples/...", "json-events") must_== ParseResult.ParseSuccess
    }
  }

  "test with json" >> {
    ParserRun.parse(CrystalParser, "parsers/crystal/test/examples/...", "json") must_== ParseResult.ParseSuccess
  }
}
