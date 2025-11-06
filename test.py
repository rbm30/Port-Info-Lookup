from port_info import port_info


def test_port_info():
    info = port_info(80)
    
    # tester
    assert info is not None, "Port 80 not found"
    assert info['port_number'] == '80'
    assert info['transport_protocol'].lower() in ['tcp', 'udp']
    print("Test Passed: Port 80 information fetched successfully")

    info_22 = port_info(22)
    assert info_22['service_name'].lower() == 'ssh', "Expected SSH for port 22"
    print("Test Passed: Port 22 (SSH) found successfully")


    # output
    print(f"Port number        : {info['port_number']}")
    print(f"Transport protocol : {info['transport_protocol']}")
    print(f"Service name       : {info['service_name']}")
    print(f"Description        : {info['description']}")


if __name__ == "__main__":
    test_port_info()