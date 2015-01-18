import scala.util.parsing.combinator._

sealed trait Element
case class Tag(name: String, attr: String) extends Element
case class Header(text: String) extends Element
case class Plain(text: String) extends Element

object parse extends RegexParsers {
  override def skipWhitespace = false
  def tag: Parser[Tag] = ("<" ~> "\\S+".r <~ "\\s".r) ~ "[^\\s>]+".r <~ ">" ^^ {
    case name ~ attr => Tag(name, attr)
  }
  def header: Parser[Header] = "\\-".r ~> "[^+]*".r <~ "+" ^^ (Header(_))
  def plain: Parser[Plain] = "[^<>\\-\\+]+".r ^^ (Plain(_))
  def elements: Parser[List[Element]] = rep(tag | header | plain)
  def apply(s: String) = parseAll(elements, s)
}

object run {
  def main(args: Array[String]) {
    var index = 1
    var print = false
    val input = io.Source.fromFile(
      "./edF.txt"
    // ).getLines.take(15522).mkString(" ") // Pars Prima 
    // ).getLines.take(59012).mkString(" ") // Pars Prima and Pars Secunda
    ).getLines.take(64523).mkString(" ") // entire file
    // parse(input).get foreach println
    parse(input).get.map {
      case Tag("1", "C") => // case start
      case Tag("1", "D") => // distinction start
      case Tag("1", "DC") => //
      case Tag("1", "DP") => //
      case Tag("2", _) => // distinction number
      case Tag("3", _) => // question number
      case Tag("4", _) => // capitulum
      case Tag("L", _) => // line
      case Tag("P", "0") => // Palea end
      case Tag("P", "1") => // Palea start
      case Tag("S", _) => // page
      case Tag("T", "A") => // dictum ante
      case Tag("T", "I") => // inscription
      case Tag("T", "P") => // dictum post
      case Tag("T", "Q") => // case statement
      case Tag("T", "R") => print = true // rubric
      case Tag("T", "T") => // text
      case Tag(_, _) => // error
      // case Tag(name, attr) => println(name + "\t" + attr)
      case Header(text) => // do nothing
      case Plain(text) => // do nothing
        val spaces = "\\s+".r
        if (print) {
          if (!spaces.pattern.matcher(text).matches) {
            // println(f"$index%04d" + " _ " + text)
            println(text.trim())
            index = index + 1
            print = false
          }
        }
    }
  }
}
