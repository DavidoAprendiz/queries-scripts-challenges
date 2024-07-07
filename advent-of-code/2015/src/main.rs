// https://adventofcode.com/2015/

pub const BLUE: &str = "\x1b[0m\x1b[34m";
pub const BLUE_BOLD: &str = "\x1b[0m\x1b[34;1;4m";
pub const CLOSE: &str = "\x1b[0m";

mod day01;
mod day02;
mod day03;

fn main() {
    day01::main();
    day02::main();
    day03::main();
}
