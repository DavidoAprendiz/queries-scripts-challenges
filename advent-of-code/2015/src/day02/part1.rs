struct Gift {
    l: u32,
    w: u32,
    h: u32,
}

impl Gift {
    fn total(&self) -> u32 {
        (2 * self.l * self.w) + (2 * self.w * self.h) + (2 * self.h * self.l) + (self.l * self.w)
    }
}

pub fn main(data: &str) -> u32 {
    let mut result = 0;
    for i in data.lines() {
        let mut my_vec: Vec<u32> = i.split('x').map(|d| d.parse::<u32>().unwrap()).collect();

        my_vec.sort();
        result += Gift {
            l: my_vec[0],
            w: my_vec[1],
            h: my_vec[2],
        }
        .total();
    }
    result
}
