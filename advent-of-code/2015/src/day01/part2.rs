pub fn main(data: &str) -> i16 {
    let mut floor = 0;
    for i in data.lines() {
        for (index, c) in i.chars().enumerate() {
            if floor < 0 {
                return index as i16;
            }
            match c {
                '(' => floor += 1,
                ')' => floor -= 1,
                _ => (),
            }
        }
    }
    0
}
