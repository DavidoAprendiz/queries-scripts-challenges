fn main() {
    println!("\nCodeWars: count_by() -> {:?}", count_by());

    println!(
        "\nCodeWars: name_shuffler() -> {:?}",
        name_shuffler("john McClane")
    );

    println!("\nCodeWars: get_grade() -> {}", get_grade(0, 0, 3));

    println!(
        "\nCodeWars: rock_paper_scissors() -> {}",
        rock_paper_scissors("rock", "rock")
    );

    println!(
        "\nCodeWars: make_upper_case() -> {}",
        make_upper_case("hello")
    );

    println!("\nCodeWars: zero_fuel() -> {}", zero_fuel(50, 25, 2));

    println!("\nCodeWars: hero() -> {}", hero(10, 5));

    println!(
        "\nCodeWars: expressions_matter() -> {}",
        expressions_matter(1, 1, 1)
    );

    println!(
        "\nCodeWars: warn_the_sheep() -> {}",
        warn_the_sheep(&["sheep", "wolf", "sheep", "sheep", "sheep", "sheep", "sheep"])
    );
}

fn count_by() -> Vec<u32> {
    let x = 50;
    let n = 5;
    let mut my_vec = vec![];

    for i in 1..=n {
        my_vec.push(x * i);
    }
    my_vec
}

fn name_shuffler(s: &str) -> String {
    let name: Vec<&str> = s.split(' ').collect();
    format!("{} {}", name[1], name[0])
}

fn get_grade(s1: u32, s2: u32, s3: u32) -> char {
    match (s1 + s2 + s3) / 3 {
        90..=100 => 'A',
        80..=89 => 'B',
        70..=79 => 'C',
        60..=79 => 'D',
        0..=59 => 'F',
        _ => ' ',
    }
}

fn rock_paper_scissors(p1: &str, p2: &str) -> &'static str {
    match (p1, p2) {
        ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock") => "Player 1 won!",
        ("scissors", "rock") | ("paper", "scissors") | ("rock", "paper") => "Player 2 won!",
        (_, _) => "Draw!",
    }
}

fn make_upper_case(s: &str) -> String {
    s.to_uppercase()
}

fn zero_fuel(distance_to_pump: u32, mpg: u32, gallons: u32) -> bool {
    if distance_to_pump <= mpg * gallons {
        true
    } else {
        false
    }
}

fn hero(bullets: u16, dragons: u16) -> bool {
    if bullets / 2 >= dragons {
        true
    } else {
        false
    }
}

fn expressions_matter(a: u64, b: u64, c: u64) -> u64 {
    // let first = a * (b + c);
    // let second = a * b * c;
    // let third = a + b * c;
    // let forth = (a + b) * c;
    // let fifth = a + b + c;

    *vec![a * (b + c), a * b * c, a + b * c, (a + b) * c, a + b + c]
        .iter()
        .max()
        .unwrap()
}

fn warn_the_sheep(queue: &[&str]) -> String {
    let mut result = String::new();
    for i in 0..queue.len() {
        if queue[i].to_string() == "wolf".to_string() {
            if queue.len() - i == 1 {
                result = format!("Pls go away and stop eating my sheep");
            } else {
                result = format!(
                    "Oi! Sheep number {}! You are about to be eaten by a wolf!",
                    queue.len() - i - 1
                );
            }
        }
    }
    result
}
