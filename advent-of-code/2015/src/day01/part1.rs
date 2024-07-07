pub fn main(data: &str) -> i16 {
    let mut floor = 0;
    for i in data.lines() {
        for c in i.chars() {
            match c {
                '(' => floor += 1,
                ')' => floor -= 1,
                _ => (),
            }
        }
    }
    floor
}
