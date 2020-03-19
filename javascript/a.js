handleFilter = (data) => {
    data.map((val) => {
    const temp = val
    temp.y3 = val.y3 > 1000 ? 0 : val.y3;
    return temp;
    });
    return data;
    };
    