package eu.nomad_lab.parsers

import org.specs2.mutable.Specification

object CrystalParserSpec extends Specification {
  "CrystalParserTest" >> {
    "test with json-events" >> {
      ParserRun.parse(CrystalParser, "parsers/crystal/test/examples/mgo/mgo.out", "json-events") must_== ParseResult.ParseSuccess
    }
  }

  "test with json" >> {
    ParserRun.parse(CrystalParser, "parsers/crystal/test/examples/mgo/mgo.out", "json") must_== ParseResult.ParseSuccess
  }
}
