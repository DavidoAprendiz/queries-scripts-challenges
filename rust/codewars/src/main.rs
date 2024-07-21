use std::ops::Neg;

fn main() {
    println!("\nCodeWars: count_by() -> {:?}", count_by(50, 5));

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

    println!(
        "\nCodeWars: split_strings() -> {:?}",
        split_strings("abcdefg")
    );

    println!("\nCodeWars: series_sum() -> {:?}", series_sum(7));

    println!(
        "\nCodeWars: count_positives_sum_negatives() -> {:?}",
        count_positives_sum_negatives(vec![1, -1, 0, -5, 5])
    );

    println!("\nCodeWars: get_age() -> {:?}", get_age("7 years old"));

    println!("\nCodeWars: digitize() -> {:?}", digitize(348597));

    println!("\nCodeWars: update_light() -> {:?}", update_light("green"));

    println!("\nCodeWars: invert() -> {:?}", invert(&[1, 2, 3, 4, 5]));

    println!("\nCodeWars: is_triangle() -> {:?}", is_triangle(1, 2, 2));

    println!("\nExercism: reverse() -> {:?}", reverse("abc"));

    println!("\nCodeWars: get_count() -> {:?}", get_count("abracadabra"));

    println!("\nCodeWars: move_hero() -> {:?}", move_hero(3, 6));

    println!("\nCodeWars: accum() -> {:?}", accum("ZpglnRxqenU"));

    println!(
        "\nCodeWars: string_to_array() -> {:?}",
        string_to_array("Robin Singh")
    );

    println!(
        "\nCodeWars: get_volume_of_cuboid() -> {:?}",
        get_volume_of_cuboid(1.0, 2.0, 3.0)
    );

    println!("\nCodeWars: get_char() -> {}", get_char(72));

    println!(
        "\nCodeWars: two_sort() -> {}",
        two_sort(&[
            "z", "bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"
        ])
    );

    println!(
        "\nCodeWars: fake_bin() -> {}",
        fake_bin("45385593107843568")
    );

    println!(
        "\nCodeWars: odd_or_even() -> {}",
        odd_or_even(vec![
            0, 1, -5, 1, 2, 31, 123, 451, 511414, 12313, 123, 3123, 451, 21, 1,
        ])
    );

    println!(
        "\nCodeWars: bin_to_decimal() -> {}",
        bin_to_decimal("1001001")
    );

    println!("\nCodeWars: hello() -> {}", hello("tEsTE"));

    println!("\nCodeWars: count_sheep() -> {}", count_sheep(2));

    println!(
        "\nCodeWars: remove_exclamation_marks() -> {}",
        remove_exclamation_marks("Testes!!! te!st!es!")
    );

    println!(
        "\nCodeWars: open_or_senior() -> {:?}",
        open_or_senior(vec![(45, 12), (55, 21), (19, -2), (104, 20)])
    );

    println!("\nCodeWars: order() -> {:?}", order("is2 Thi1s T4est 3a"));

    println!(
        "\nCodeWars: find_difference() -> {:?}",
        find_difference(&[3, 2, 5], &[1, 4, 4])
    );

    println!("\n");
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

fn count_by(x: u32, n: u32) -> Vec<u32> {
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
        return true;
    }
    false
}

fn hero(bullets: u16, dragons: u16) -> bool {
    if bullets / 2 >= dragons {
        return true;
    }
    false
}

fn expressions_matter(a: u64, b: u64, c: u64) -> u64 {
    // let first = a * (b + c);
    // let second = a * b * c;
    // let third = a + b * c;
    // let forth = (a + b) * c;
    // let fifth = a + b + c;

    *[a * (b + c), a * b * c, a + b * c, (a + b) * c, a + b + c]
        .iter()
        .max()
        .unwrap()
}

fn warn_the_sheep(queue: &[&str]) -> String {
    let mut result = String::new();
    for i in 0..queue.len() {
        if String::from(queue[i]).contains("wolf") {
            if queue.len() - i == 1 {
                result = "Pls go away and stop eating my sheep".to_string();
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

fn split_strings(s: &str) -> Vec<String> {
    let mut my_vec = Vec::new();
    let mut my_vec2 = Vec::new();
    let mut counter = 0;
    let mut word = String::new();

    for i in s.chars() {
        my_vec.push(i.to_string())
    }

    while counter != my_vec.len() {
        word.push_str(&my_vec[counter].to_owned());
        if counter % 2 == 1 {
            my_vec2.push(word.clone());
            word = String::new();
        }

        counter += 1;
    }
    if !word.is_empty() {
        my_vec2.push(word + "_");
    }
    my_vec2
}

fn series_sum(n: u32) -> String {
    match n {
        0 => "0.00".to_string(),
        _ => {
            let mut denominator: f64 = 1.00;
            let mut result: f64 = 1.00;

            for _ in 1..n {
                denominator += 3.00;
                result += 1.00 / (denominator);
            }
            format!("{:.2}", result)
        }
    }
}

fn count_positives_sum_negatives(input: Vec<i32>) -> Vec<i32> {
    let mut count = 0;
    let mut sum = 0;
    let mut my_vec = Vec::new();

    if input.is_empty() {
        return my_vec;
    }
    for num in input {
        match num {
            num if num > 0 => count += 1,
            num if num < 0 => sum += num,
            _ => (),
        }
    }
    my_vec.push(count);
    my_vec.push(sum);
    my_vec
}

fn get_age(age: &str) -> u32 {
    age.split_ascii_whitespace()
        .next()
        .unwrap()
        .parse::<u32>()
        .unwrap()
}

fn digitize(n: u64) -> Vec<u8> {
    let mut my_vec = Vec::new();
    for i in n.to_string().chars().rev() {
        my_vec.push(i.to_digit(10).unwrap() as u8)
    }
    my_vec
}

fn update_light(current: &str) -> String {
    match current {
        "green" => "yellow",
        "yellow" => "red",
        "red" => "green",
        _ => "",
    }
    .into()
}

fn invert(values: &[i32]) -> Vec<i32> {
    let mut my_vec = Vec::new();
    for i in values.iter() {
        my_vec.push(i.neg());
    }
    my_vec
}

fn is_triangle(a: i64, b: i64, c: i64) -> bool {
    if (a + b > c) && (a + c > b) && (b + c > a) {
        return true;
    }
    false
}

// Exercism
fn reverse(input: &str) -> String {
    input.chars().rev().collect()
}

fn get_count(string: &str) -> usize {
    let mut vowels_count: usize = 0;

    // test1
    for i in string.chars() {
        match i {
            'a' => vowels_count += 1,
            'e' => vowels_count += 1,
            'i' => vowels_count += 1,
            'o' => vowels_count += 1,
            'u' => vowels_count += 1,
            _ => (),
        }
    }
    // test2
    for i in string.chars() {
        match i {
            char if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' => {
                vowels_count += 1
            }
            _ => (),
        }
    }
    // test3
    vowels_count = 0; // reset after test 1 e 2
    for i in string.chars() {
        match i {
            'a' | 'e' | 'i' | 'o' | 'u' => vowels_count += 1,
            _ => (),
        }
    }

    vowels_count
}

fn move_hero(position: u32, roll: u32) -> u32 {
    position + roll * 2
}

fn accum(s: &str) -> String {
    let mut my_string = String::new();

    for (i, c) in s.chars().enumerate() {
        let a = &String::from(c).to_uppercase();
        my_string += a;
        my_string += &a.repeat(i).to_lowercase().to_string();
        if i != s.len() - 1 {
            my_string += "-";
        }
    }
    my_string
}

fn string_to_array(s: &str) -> Vec<String> {
    let mut my_vec = vec![];
    for i in s.split(' ') {
        my_vec.push(i.to_owned());
    }

    my_vec
}

fn get_volume_of_cuboid(length: f32, width: f32, height: f32) -> f32 {
    length * width * height
}

fn get_char(c: i32) -> char {
    std::char::from_u32(c as u32).unwrap()
}

fn two_sort(arr: &[&str]) -> String {
    let mut my_vec: Vec<_> = vec![];
    for l in arr {
        my_vec.push(l)
    }
    my_vec.sort();

    let mut final_word: String = "".to_string();
    let mut word_length = my_vec[0].len();

    for c in my_vec[0].chars() {
        final_word.push(c);
        word_length -= 1;
        if word_length == 0 {
            break;
        }
        final_word.push_str("***");
    }
    final_word
}
fn fake_bin(s: &str) -> String {
    let mut my_string = String::new();
    for c in s.chars() {
        if c.to_digit(10).unwrap() < 5 {
            my_string.push('0')
        } else {
            my_string.push('1')
        }
    }
    my_string
}

fn odd_or_even(numbers: Vec<i32>) -> String {
    let mut result = 0;
    for n in numbers {
        result += n;
    }
    if result % 2 == 0 {
        "is even".to_string()
    } else {
        "is odd".to_string()
    }
}

fn bin_to_decimal(inp: &str) -> i32 {
    i32::from_str_radix(inp, 2).unwrap()
}

fn hello(name: &str) -> String {
    match name {
        n if !n.is_empty() => format!(
            "Hello, {}{}",
            n[..1].to_ascii_uppercase(),
            n[1..].to_ascii_lowercase()
        ),
        _ => "".to_string(),
    }
}

fn count_sheep(n: u32) -> String {
    if n == 0 {
        return "".to_string();
    }
    let mut my_string = String::new();
    for i in 1..(n + 1) {
        my_string.push_str(i.to_string().as_str());
        my_string.push_str(" sheep...")
    }
    my_string
}

fn remove_exclamation_marks(input: &str) -> String {
    input.replace('!', "")
}

fn open_or_senior(data: Vec<(i32, i32)>) -> Vec<String> {
    let mut my_vec = vec![];
    for (age, hand) in data {
        if age >= 55 && hand > 7 {
            my_vec.push("Senior".to_string())
        } else {
            my_vec.push("Open".to_string())
        }
    }
    my_vec
}

fn order(sentence: &str) -> String {
    let mut words: Vec<&str> = sentence.split(' ').collect();
    let mut count = 0;
    while count != words.len() + 1 {
        words.sort_by_key(|a| a.contains(&count.to_string()));
        count += 1;
    }
    let mut my_string = String::new();
    for w in &words {
        my_string.push_str(w);
        if w == words.last().unwrap() {
            break;
        }
        my_string.push(' ');
    }
    // for i in 0..my_string.len() {
    //     my_string = my_string.replace(&i.to_string(), "");
    // }
    my_string
}

fn find_difference(a: &[i32; 3], b: &[i32; 3]) -> i32 {
    (a[0] * a[1] * a[2] - b[0] * b[1] * b[2]).abs()
}
