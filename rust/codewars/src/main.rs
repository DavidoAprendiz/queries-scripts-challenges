use either::Either;
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

    println!("\nCodeWars: order() -> {}", order("is2 Thi1s T4est 3a"));

    println!(
        "\nCodeWars: find_difference() -> {}",
        find_difference(&[3, 2, 5], &[1, 4, 4])
    );

    println!("\nCodeWars: xo() -> {}", xo("xo"));

    println!("\nCodeWars: combat() -> {}", combat(200.0, 30.0));

    println!(
        "\nCodeWars: to_alternating_case() -> {}",
        to_alternating_case("hello world")
    );

    println!("\nCodeWars: tower_builder() -> {:?}", tower_builder(16));

    println!("\nCodeWars: number() -> {:?}", number(&["a", "b", "c"]));

    println!("\nCodeWars: abbrev_name() -> {}", abbrev_name("Sam Harris"));

    println!("\nCodeWars: expanded_form() -> {}", expanded_form(42));

    println!("\nCodeWars: basic_op() -> {}", basic_op('+', 4, 7));

    println!(
        "\nCodeWars: sum_mix() -> {}",
        sum_mix(&[
            Either::Left(9),
            Either::Left(3),
            Either::Right("7".to_string()),
            Either::Right("3".to_string()),
            Either::Right("None".to_string())
        ])
    );

    println!("\nCodeWars: double_char() -> {}", double_char("testing"));

    println!("\nCodeWars: dna_to_rna() -> {}", dna_to_rna("TGTT"));

    println!(
        "\nCodeWars: no_space() -> {}",
        no_space("8 j 8   mBliB8g  imjB8B8  jl  B".to_string())
    );

    println!("\nCodeWars: likes() -> {}", likes(&["Jacob", "Alex"]));

    println!("\nCodeWars: multi_table() -> {}", multi_table(5));

    println!("\nCodeWars: is_it_letter() -> {}", is_it_letter('f'));

    println!("\nCodeWars: count_red_beads() -> {}", count_red_beads(6));

    println!(
        "\nCodeWars: remove_every_other() -> {:?}",
        remove_every_other(&[1, 2, 3, 4, 5, 6, 7])
    );

    println!("\nCodeWars: greet() -> {}", greet("english"));

    println!(
        "\nCodeWars: find_short() -> {}",
        find_short("bitcoin take over the world maybe who knows perhaps")
    );

    println!("\nCodeWars: duty_free() -> {}", duty_free(12, 50, 1000));

    println!(
        "\nCodeWars: sum_two_smallest_numbers() -> {}",
        sum_two_smallest_numbers(&[15, 28, 4, 2, 43])
    );

    println!(
        "\nCodeWars: get_drink_by_profession() -> {}",
        get_drink_by_profession("jabrOni")
    );

    println!("\nCodeWars: set_alarm() -> {}", set_alarm(true, false));

    println!(
        "\nCodeWars: check_exam() -> {}",
        check_exam(&["a", "a", "b", "b"], &["a", "c", "b", "d"])
    );
    println!(
        "\nCodeWars: unique_in_order() -> {:?}",
        unique_in_order("AAAABBBCCDAABBB".chars())
    );

    println!("\nCodeWars: validate_pin() -> {}", validate_pin("090909"));

    println!("\nCodeWars: greet2() -> {}", greet2("name", "name"));

    println!("\nCodeWars: add_length() -> {:?}", add_length("apple ban"));

    println!("\nCodeWars: hex_to_dec() -> {}", hex_to_dec("A"));

    println!("\nCodeWars: min_value() -> {}", min_value(vec![1, 3, 1]));

    println!(
        "\nCodeWars: sort_numbers() -> {:?}",
        sort_numbers(&[1, 2, 3, 10, 5])
    );

    println!("\n");
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

fn xo(string: &'static str) -> bool {
    if !string.to_lowercase().to_string().contains('x')
        && !string.to_lowercase().to_string().contains('o')
    {
        true
    } else {
        string
            .chars()
            .filter(|f| f.to_lowercase().to_string() == "x")
            .count()
            == string
                .chars()
                .filter(|f| f.to_lowercase().to_string() == "o")
                .count()
    }
}

fn combat(health: f32, damage: f32) -> f32 {
    if health - damage < 0.0 {
        return 0.0;
    }
    health - damage
}

fn to_alternating_case(s: &str) -> String {
    let mut final_string: String = String::new();
    for c in s.chars() {
        if c.is_ascii_lowercase() {
            final_string.push_str(c.to_uppercase().to_string().as_str())
        } else {
            final_string.push_str(c.to_lowercase().to_string().as_str())
        }
    }
    final_string
}

fn tower_builder(n_floors: usize) -> Vec<String> {
    let mut my_vec: Vec<String> = vec![];
    let mut spaces = " ".repeat(n_floors - 1);
    if n_floors == 1 {
        my_vec.push(String::from("*"));
        return my_vec;
    }
    for (counter, n) in (1..n_floors + 1).enumerate() {
        my_vec.push(spaces.clone());
        my_vec[n - 1].push_str("*".repeat(n + counter).as_str());
        my_vec[n - 1].push_str(spaces.clone().as_str());
        if !spaces.is_empty() {
            spaces.pop().unwrap();
        }
        // counter += 1;
    }
    // println!("\n");
    // for i in my_vec.iter() {
    //     println!("{}", i)
    // }
    my_vec
}

fn number(lines: &[&str]) -> Vec<String> {
    let mut my_vec = vec![];
    for (i, l) in lines.iter().enumerate() {
        my_vec.push(format!("{}: {}", i + 1, l));
    }
    my_vec
}

fn abbrev_name(name: &str) -> String {
    let my_string: Vec<&str> = name.split(' ').collect();
    format!(
        "{}.{}",
        my_string[0].chars().next().unwrap().to_uppercase(),
        my_string[1].chars().next().unwrap().to_uppercase(),
    )
}

fn expanded_form(n: u64) -> String {
    let mut n_length = n.to_string().len();
    let mut my_string = String::new();

    for num in n.to_string().chars() {
        n_length = n_length.saturating_sub(1);
        if num != '0' {
            my_string.push_str(format!("{}{} ", num, "0".repeat(n_length)).as_str())
        }
    }
    my_string = my_string[..my_string.len() - 1].replace(' ', " + ");
    my_string
}

fn basic_op(operator: char, value1: i32, value2: i32) -> i32 {
    match operator {
        '+' => value1 + value2,
        '-' => value1 - value2,
        '*' => value1 * value2,
        '/' => value1 / value2,
        _ => 0,
    }
}

fn sum_mix(arr: &[Either<i32, String>]) -> i32 {
    let mut my_num: i32 = 0;
    for n in arr.iter() {
        if n.is_left() {
            my_num += n.clone().unwrap_left()
        } else if n.is_right() {
            for num in n.clone().unwrap_right().chars() {
                if !num.is_alphabetic() {
                    my_num += num.to_digit(10).unwrap() as i32
                }
            }
        }
    }
    my_num
}

fn double_char(s: &str) -> String {
    s.chars().map(|c| c.to_string().repeat(2)).collect()
}

fn dna_to_rna(dna: &str) -> String {
    dna.replace('T', "U")
}

fn no_space(x: String) -> String {
    x.split_ascii_whitespace().collect()
}

fn likes(names: &[&str]) -> String {
    match names.len() {
        0 => "no one likes this".to_string(),
        1 => format!("{} likes this", names[0]),
        2 => format!("{} and {} likes this", names[0], names[1]),
        3 => format!("{}, {} and {} likes this", names[0], names[1], names[2]),
        _ => format!(
            "{}, {} and {} others likes this",
            names[0],
            names[1],
            names.len() - 2
        ),
    }
}
fn multi_table(n: u64) -> String {
    let mut my_str: String = String::new();
    for i in 1..=10 {
        my_str.push_str(format!("{} * {} = {}", i, n, n * i).as_str());
        if i != 10 {
            my_str.push('\n');
        }
    }
    my_str
}

fn is_it_letter(c: char) -> bool {
    c.is_alphabetic()
}

fn count_red_beads(n: u32) -> u32 {
    if n < 2 {
        return 0;
    }
    (n * 2) - 2
}

fn remove_every_other(arr: &[u8]) -> Vec<u8> {
    let mut my_arr = vec![];
    for (i, num) in arr.iter().enumerate() {
        if i % 2 == 0 {
            my_arr.push(num.to_owned())
        }
    }
    my_arr
}

fn greet(language: &str) -> &str {
    let db = [
        ("english", "Welcome"),
        ("czech", "Vitejte"),
        ("danish", "Velkomst"),
        ("dutch", "Welkom"),
        ("estonian", "Tere tulemast"),
        ("finnish", "Tervetuloa"),
        ("flemish", "Welgekomen"),
        ("french", "Bienvenue"),
        ("german", "Willkommen"),
        ("irish", "Failte"),
        ("italian", "Benvenuto"),
        ("latvian", "Gaidits"),
        ("lithuanian", "Laukiamas"),
        ("polish", "Witamy"),
        ("spanish", "Bienvenido"),
        ("swedish", "Valkommen"),
        ("welsh", "Croeso"),
    ];

    for lang in db {
        if lang.0 == language {
            return lang.1;
        }
    }
    "Welcome"
}

fn find_short(s: &str) -> u32 {
    let mut min_num = 999;
    //your code here
    for l in s.split(' ') {
        if l.len().lt(&min_num) {
            min_num = l.len();
        }
    }
    min_num as u32
}

fn duty_free(price: i32, discount: i32, holiday_cost: i32) -> i32 {
    (holiday_cost as f32 / (price as f32 * (discount as f32 / 100.0))) as i32
}

fn sum_two_smallest_numbers(numbers: &[u32]) -> u32 {
    let mut my_vec = numbers.to_owned();
    my_vec.sort();
    my_vec[0] + my_vec[1]
}

fn get_drink_by_profession(param: &str) -> &'static str {
    match param.to_lowercase().as_str() {
        "jabroni" => "Patron Tequila",
        "school counselor" => "Anything with Alcohol",
        "programmer" => "Hipster Craft Beer",
        "bike gang member" => "Moonshine",
        "politician" => "Your tax dollars",
        "rapper" => "Cristal",
        _ => "Beer",
    }
}

fn set_alarm(employed: bool, vacation: bool) -> bool {
    matches!((employed, vacation), (true, false))
}

fn check_exam(arr_a: &[&str], arr_b: &[&str]) -> i64 {
    let mut total = 0;
    for i in 0..4 {
        match () {
            _ if arr_b[i].is_empty() => total += 0,
            _ if arr_a[i].ne(arr_b[i]) => total -= 1,
            _ if arr_a[i].eq(arr_b[i]) => total += 4,
            _ => total += 0,
        }
    }
    if total <= 0 {
        0
    } else {
        total
    }
}

fn unique_in_order<T>(sequence: T) -> Vec<T::Item>
where
    T: std::iter::IntoIterator,
    T::Item: std::cmp::PartialEq + std::fmt::Debug,
{
    let mut my_vec: Vec<_> = vec![];
    for s in sequence.into_iter() {
        if !my_vec.is_empty() {
            if my_vec.last().unwrap() != &s {
                my_vec.push(s)
            }
        } else {
            my_vec.push(s)
        }
    }
    my_vec
}

fn validate_pin(pin: &str) -> bool {
    if pin.len() == 6 || pin.len() == 4 {
        for p in pin.chars() {
            if !p.is_ascii_digit() {
                return false;
            }
        }
        return true;
    }
    false
}

fn greet2(name: &str, owner: &str) -> String {
    if name == owner {
        "Hello boss".to_string()
    } else {
        "Hello guest".to_string()
    }
}

fn add_length(s: &str) -> Vec<String> {
    s.split_whitespace()
        .map(|x| format!("{} {}", x, x.len()))
        .collect()
}

fn hex_to_dec(hex_string: &str) -> u32 {
    u32::from_str_radix(hex_string, 16).unwrap()
}

fn min_value(mut digits: Vec<i32>) -> i32 {
    digits.sort();
    digits.dedup();
    digits
        .iter()
        .map(|x| x.to_string())
        .collect::<String>()
        .parse::<i32>()
        .unwrap()
}

fn sort_numbers(arr: &[i32]) -> Vec<i32> {
    let mut my_vec: Vec<i32> = arr.to_owned();
    my_vec.sort();
    my_vec
}
