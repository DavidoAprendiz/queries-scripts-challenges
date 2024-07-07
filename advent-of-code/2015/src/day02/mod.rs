mod part1;
mod part2;
use crate::BLUE;
use crate::BLUE_BOLD;
use crate::CLOSE;

pub fn main() {
    let file = include_str!("input.txt");

    println!("\n{BLUE_BOLD}Day 2{CLOSE}");
    println!("Part 1 -> {BLUE}{:?}{CLOSE}", part1::main(file));
    println!("Part 2 -> {BLUE}{:?}{CLOSE}", part2::main(file));
}
