from client import ResponsiveWireframeComponentLayoutGeneratorClient

def main():
    client = ResponsiveWireframeComponentLayoutGeneratorClient()
    res = client.generate_wireframe_tree('Mobile onboarding flow', 390)
    print('Wireframe Component Layout Generator: ' + res['wireframe_id'] + ' (' + res['viewport_mode'] + ')')
    print('Components: ' + str(len(res['component_tree'])) + ' elements | Padding: ' + str(res['auto_layout_padding_px']) + 'px')
    print('Canvas JSON URL: ' + res['wireframe_canvas_json_url'])

if __name__ == '__main__':
    main()
